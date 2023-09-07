import React, { useState, useEffect } from 'react';
import DateInput from './DateInput';
import Container from '@mui/material/Container';
import dayjs from 'dayjs';
import SelectField from './SelectField';
import CheckBox from './CheckBox';
import { Button } from '@mui/material';
import Grid from '@mui/material/Grid';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import ListPage from '../pages/List';
import { useLocation } from 'react-router-dom';
import CalendarPage from '../pages/Calendar';

const currentRawDate = dayjs();
const currentDate = dayjs();
const dayFromCurrentDate = currentRawDate.add(1, 'days');
const frequencies = [
  'Weekly',
  'Biweekly',
  'Monthly',
  'Bimonthly',
  'Quarterly',
  'Semi-Annually',
  'Annually',
];

const countries = ['Australia', 'Brazil', 'Germany', 'Italy', 'South Africa', 'United States'];
const businessRules = [
  'Following',
  'Preceding',
  'Modified Following',
  'Modified Preceding',
  'No Adjustment',
];

const Alert = React.forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant='filled' {...props} />;
});

const utc = require('dayjs/plugin/utc');
const timezone = require('dayjs/plugin/timezone'); // dependent on utc plugin
dayjs.extend(utc);
dayjs.extend(timezone);

const timeZone = dayjs.tz.guess();

function Form() {
  const [isToggled, setIsToggled] = useState(false);
  const [value, setValue] = useState('');
  const [valid, setValid] = useState(false);
  const [open, setOpen] = useState(false);

  const [state, setState] = useState({
    startDate: currentDate,
    endDate: dayFromCurrentDate,
    minimumEndDate: dayFromCurrentDate,
    frequency: 'Weekly',
    country: 'United States',
    businessDayRule: 'Following',
    endOfMonthRule: false,
    timeZone: timeZone,
  });

  const updateStartDate = (newValue) => {
    setState((prevState) => {
      return { ...prevState, startDate: newValue };
    });
  };

  const updateEndDate = (newValue) => {
    setState((prevState) => {
      return { ...prevState, endDate: newValue };
    });
  };

  const updateMinimumEndDate = (newValue) => {
    setState((prevState) => {
      return { ...prevState, minimumEndDate: newValue };
    });
  };

  const updateFrequency = (newValue) => {
    setState((prevState) => {
      return {
        ...prevState,
        frequency: newValue,
      };
    });
  };

  const updateBusinessDayRule = (newValue) => {
    setState((prevState) => {
      return {
        ...prevState,
        businessDayRule: newValue.target.value,
      };
    });
  };
  const updateCountry = (newValue) => {
    setState((prevState) => {
      return {
        ...prevState,
        country: newValue.target.value,
      };
    });
  };

  const toggleEndOfMonthRule = () => {
    setState((prevState) => {
      return { ...prevState, endOfMonthRule: !prevState.endOfMonthRule };
    });
  };

  const disableEndOfMonthRule = () => {
    setState((prevState) => {
      return { ...prevState, endOfMonthRule: false };
    });
  };

  const handleValidation = (event, values) => {
    if (frequencies.includes(values) === true) {
      setValid(true);
      setValue(values);
    } else {
      const reg = new RegExp('\\b[1-9]{1}[0-9]*[d,w,m,y,D,W,M,Y]{1}\\b');
      setValid(reg.test(values));
      setValue(values);
    }
    updateFrequency(values);
  };

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpen(false);
  };

  const handleClick = () => {
    if (valid) {
      setIsToggled(true);

      if (
        !frequencies.includes(value) &&
        !frequencies.includes(value.toLowerCase()) &&
        !frequencies.includes(value.toUpperCase())
      ) {
        frequencies.push(value);
      }
    } else {
      setOpen(true);
      setIsToggled(false);
    }

    // var sdate = state.startDate.toDate();
    // var new_startDate = sdate.getTime() - (sdate.getTimezoneOffset() * 60000);
    // setState((prevState) => {
    //   return { ...prevState, startDate: sdate};
    // });
  };

  useEffect(() => {
    const minEndDate = state.startDate.add(1, 'day');
    if (state.endDate.diff(state.startDate, 'day') < 1) {
      updateEndDate(minEndDate);
    }
    updateMinimumEndDate(minEndDate);
  }, [state.startDate]);

  const [dateList, setDateList] = useState([]);
  const [holidayList, setHolidayList] = useState([]);

  const fetchDateList = async () => {
    const res = await fetch('/dates');
    setDateList(await res.json());
  };

  const fetchHolidaysList = async () => {
    let holidaysArray = [[]];
    const res = await fetch('/holidays');
    let json = await res.json();
    Object.entries(json).forEach(([key, value]) => holidaysArray.push([key, value]));
    holidaysArray.splice(0, 1);
    setHolidayList(holidaysArray);
  };

  const path = useLocation().pathname;

  return (
    <Container sx={{ marginTop: '25px' }}>
      <Grid container spacing={2} justifyContent='center' alignItems='center'>
        <Grid item xs={6} sm={2.4}>
          <DateInput label={'Start Date'} value={state.startDate} onChange={updateStartDate} />
        </Grid>
        <Grid item xs={6} sm={2.4}>
          <DateInput
            label={'End Date'}
            value={state.endDate}
            minimumDate={state.minimumEndDate}
            onChange={updateEndDate}
          />
        </Grid>
        <Grid item xs={6} sm={2.4}>
          <Autocomplete
            title={'Frequency'}
            freeSolo
            options={frequencies.map((option) => option)}
            onInputChange={handleValidation}
            renderInput={(params) => <TextField {...params} label='Frequency' value={value} />}
          />
        </Grid>
        <Grid item xs={6} sm={2.4}>
          <SelectField
            title={'Country'}
            value={state.country}
            onChange={updateCountry}
            list={countries}
          />
        </Grid>
        <Grid item xs={8} sm={2.4}>
          <SelectField
            title={'Business Day Rule'}
            value={state.businessDayRule}
            onChange={updateBusinessDayRule}
            list={businessRules}
          />
        </Grid>
        <Grid item xs={7} sm={12} style={{ textAlign: 'center' }}>
          <CheckBox
            endOfMonthRule={state.endOfMonthRule}
            disableEndOfMonthRule={disableEndOfMonthRule}
            toggleEndOfMonthRule={toggleEndOfMonthRule}
            freq={state.frequency}
            startDate={state.startDate}
            frequencyList={frequencies}
          />
        </Grid>
        <Grid item xs={7} sm={12} style={{ textAlign: 'center' }}>
          <Button
            variant='contained'
            onClick={async () => {
              handleClick();

              if (valid) {
                const dayjsStartDate = dayjs(state.startDate).format('YYYY-MM-DD');
                const dayjsEndDate = dayjs(state.endDate).format('YYYY-MM-DD');
                const dates = { state };
                const inputData = [dates, dayjsStartDate, dayjsEndDate];
                const response = await fetch('/add_dates', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                  },
                  body: JSON.stringify(inputData),
                });
                if (response.ok) {
                  fetchDateList();
                  fetchHolidaysList();
                }
              }
            }}
          >
            Calculate
          </Button>
          <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
            <Alert onClose={handleClose} severity='error' sx={{ width: '100%' }}>
              Please input the frequency as a number followed by either d, w, m, or y (day, week,
              month, year)
            </Alert>
          </Snackbar>
        </Grid>
        <ListPage
          startDate={state.startDate}
          endDate={state.endDate}
          frequency={state.frequency}
          country={state.country}
          businessDayRule={state.businessDayRule}
          endOfMonthRule={state.endOfMonthRule}
          dateList={dateList}
          active={isToggled && path === '/'}
        />
        <CalendarPage
          dateList={dateList}
          active={isToggled && path === '/calendar'}
          holidaysList={holidayList}
        />
      </Grid>
    </Container>
  );
}

export default Form;
