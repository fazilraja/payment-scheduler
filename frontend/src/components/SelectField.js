import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import FormControl from '@mui/material/FormControl';

function SelectField(props) {
  return (
    <FormControl fullWidth sx={{ m: 1 }}>
      <InputLabel>{props.title}</InputLabel>
      <Select onChange={props.onChange} label={props.title} value={props.value}>
        {props.list?.map((item) => (
          <MenuItem key={item} value={item}>
            {item}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}

export default SelectField;
