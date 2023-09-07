import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import React from 'react';
import TextField from '@mui/material/TextField';

function DateInput(props) {
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <DatePicker
        label={props.label}
        inputFormat='MM/DD/YYYY'
        value={props.value}
        onChange={props.onChange}
        minDate={props.minimumDate}
        desktopModeMediaQuery={'@media (min-width: 1224px)'}
        renderInput={(params) => <TextField style={{ margin: '8px 10px' }} {...params} />}
      />
    </LocalizationProvider>
  );
}

export default DateInput;
