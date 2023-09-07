import * as React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import ToolBar from './ToolBar';

function createData(rawDate, formattedDate) {
  return { formattedDate, rawDate };
}


export default function OutputList(props) {
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const data = [];
  const obj = JSON.parse(JSON.stringify(props.dateList));
  for (let x in obj.dateList){
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var month = ["January","February","March","April","May","June","July","August",
    "September","October","November","December"];

    //Splits up date string to input proper format for javascript date
    var dateSplit = obj.dateList[x].split("-");
    var dateString = dateSplit[2] + '/' + dateSplit[0] + '/' + dateSplit[1];  
    var formattedDate = new Date(dateString);

    var day = days[formattedDate.getDay()]
    var month = month[formattedDate.getMonth()]
    var formattedDateString = formattedDate.toString();
    var fdateSplit = formattedDateString.split(" ");
    formattedDateString = day + ', ' + month + ' ' + fdateSplit[2].replace(/-0+/g,'') + ', ' + fdateSplit[3];
    data.push(createData(formattedDateString, obj.dateList[x]));
  }

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  return (
    <Paper>
      <ToolBar
        title='Payment Dates'
        data={data}
        startDate={props.startDate}
        endDate={props.endDate}
        frequency={props.frequency}
        country={props.country}
        businessDayRule={props.businessDayRule}
        endOfMonthRule={props.endOfMonthRule}
      />
      <TableContainer>
        <Table stickyHeader aria-label='sticky table'>
          <TableHead>
            <TableRow>
              <TableCell
                sx={{
                  border: 1,
                  borderColor: 'black',
                  fontWeight: 'bold',
                  fontSize: 15,
                  backgroundColor: '#1976d2',
                  color: 'white',
                }}
                align='center'
                style={{ width: 200 }}
              >
                Formatted Date
              </TableCell>
              <TableCell
                sx={{
                  border: 1,
                  borderLeft: 0,
                  borderColor: 'black',
                  fontWeight: 'bold',
                  fontSize: 15,
                  backgroundColor: '#1976d2',
                  color: 'white',
                }}
                align='center'
                style={{ width: 200 }}
              >
                Date (MM-DD-YYYY)
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(rowsPerPage > 0
              ? data.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              : data
            ).map((data) => (
              <TableRow key={data.formattedDate}>
                <TableCell
                  sx={{ borderRight: 1, borderLeft: 1 }}
                  style={{ width: 200 }}
                  align='center'
                >
                  {data.rawDate}
                </TableCell>
                <TableCell
                  sx={{ borderRight: 1, borderLeft: 0 }}
                  style={{ width: 200 }}
                  align='center'
                >
                  {data.formattedDate}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[5, 10, 25, { label: 'All', value: -1 }]}
        component='div'
        count={data.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
        sx={{ border: 1 }}
      />
    </Paper>
  );
}