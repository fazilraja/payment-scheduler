import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import IconButton from '@mui/material/IconButton';

function ToolBar(props) {
  const handleDownload = () => {
    const array = [];
    array.push(['Formatted Date', 'Raw Date']);
    props.data.forEach((entry) => {
      array.push(Object.values(entry));
    });

    let csv = array[0][0] + ',' + array[0][1] + '\n'; // Add header
    for (let i = 1; i < array.length; i++) {
      let currentLine = '';
      for (let j = 1; j >= 0; j--) {
        if (j === 0) {
          currentLine += ',' + array[i][j];
        } else {
          currentLine += '"' + array[i][j] + '"'; // Ignore commas that are inside the formatted date by enclosing in double quotes
        }
      }
      csv += currentLine + '\n';
    }

    const startDate = new Date(props.startDate);
    const startMonth = startDate.getMonth() + 1;
    const startDay = startDate.getDate();
    const startYear = startDate.getFullYear();

    const endDate = new Date(props.endDate);
    const endMonth = endDate.getMonth() + 1;
    const endDay = endDate.getDate();
    const endYear = endDate.getFullYear();

    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8,' });
    const url = URL.createObjectURL(blob);
    const ref = document.createElement('a');
    const formattedCountry = props.country.replace(' ', '-');
    const formattedBusRule = props.businessDayRule.replace(' ', '-');
    ref.download = `Payments_${startMonth}-${startDay}-${startYear}_to_${endMonth}-${endDay}-${endYear}_Frequency=${props.frequency}_Country=${formattedCountry}_BusinessRule=${formattedBusRule}_EndOfMonthRule=${props.endOfMonthRule}`;
    ref.href = url;
    ref.click();
  };
  return (
    <Toolbar
      sx={{
        border: 1,
        borderBottom: 0,
        borderColor: 'black',
        fontWeight: 'bold',
        fontSize: 15,
        backgroundColor: '#1976d2',
        color: 'white',
      }}
    >
      <Typography variant='h5'>{props.title}</Typography>
      <IconButton
        sx={{ color: 'white', position: 'absolute', right: 0, fontWeight: 'bold', fontSize: 16 }}
        onClick={handleDownload}
      >
        Export
        <FileDownloadIcon />
      </IconButton>
    </Toolbar>
  );
}

export default ToolBar;