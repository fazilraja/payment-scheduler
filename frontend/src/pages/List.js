import OutputList from '../components/OutputList';
import Grid from '@mui/material/Grid';

function ListPage(props) {
  return (
    props.active && (
      <Grid item xs={12} sm={12} sx={{ marginBottom: '25px' }}>
        <OutputList
          startDate={props.startDate}
          endDate={props.endDate}
          frequency={props.frequency}
          country={props.country}
          businessDayRule={props.businessDayRule}
          endOfMonthRule={props.endOfMonthRule}
          dateList = {props.dateList}
        />
      </Grid>
    )
  );
}
export default ListPage;
