import React, { useState, useEffect } from 'react';
import { Checkbox } from '@mui/material';
import FormControlLabel from '@mui/material/FormControlLabel';
import dayjs from 'dayjs';

function CheckBox(props) {
  const [disabledValue, setDisabledValue] = useState(false);

  const freqIsMultipleOfMonth = () => {
    const dayRegExp = new RegExp('\\b[1-9]{1}[0-9]*[d,D]{1}\\b');
    const weekRegExp = new RegExp('\\b[1-9]{1}[0-9]*[w,W]{1}\\b');
    if (dayRegExp.test(props.freq) || weekRegExp.test(props.freq)) {
      let numberSubstringOfFrequency = props.freq.substring(0, props.freq.length - 1); // Remove last character
      let parsedIntegerSubstring = parseInt(numberSubstringOfFrequency);
      if (
        (dayRegExp.test(props.freq) && parsedIntegerSubstring >= 30) ||
        (weekRegExp.test(props.freq) && parsedIntegerSubstring >= 4)
      ) {
        return true;
      }
    }
    const monthRegExp = new RegExp('\\b[1-9]{1}[0-9]*[m,M]{1}\\b');
    const yearRegExp = new RegExp('\\b[1-9]{1}[0-9]*[y,Y]{1}\\b');
    return (
      monthRegExp.test(props.freq) ||
      yearRegExp.test(props.freq) ||
      props.freq === 'Monthly' ||
      props.freq === 'Bimonthly' ||
      props.freq === 'Quarterly' ||
      props.freq === 'Semi-Annually' ||
      props.freq === 'Annually'
    );
  };

  useEffect(() => {
    const endOfMonthForStartDate = dayjs(props.startDate).endOf('month');
    const startDateIsOtherThanEndOfMonth =
      endOfMonthForStartDate.diff(props.startDate, 'day') !== 0;
    const hasMultipleOfMonthFrequency = freqIsMultipleOfMonth();

    if (startDateIsOtherThanEndOfMonth || !hasMultipleOfMonthFrequency) {
      props.disableEndOfMonthRule();
      setDisabledValue(true);
    } else if (hasMultipleOfMonthFrequency) {
      setDisabledValue(false);
    }
  }, [props.startDate, props.freq]);

  return (
    <FormControlLabel
      control={
        <Checkbox
          checked={props.endOfMonthRule}
          onChange={props.toggleEndOfMonthRule}
          disabled={disabledValue}
        />
      }
      label='End of Month Rule'
    />
  );
}

export default CheckBox;
