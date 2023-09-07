import { Calendar, dayjsLocalizer } from 'react-big-calendar';
import dayjs from 'dayjs';
import style from 'react-big-calendar/lib/css/react-big-calendar.css';
import useMediaQuery from '@mui/material/useMediaQuery';
import Snackbar from '@mui/material/Snackbar';
import Alert from '@mui/material/Alert';
import { useState, useEffect } from 'react';

function createEvents(title, start, end) {
  return { title, start, end };
}
const localizer = dayjsLocalizer(dayjs);

function CalendarPage(props) {
  const smallDevice = useMediaQuery('(max-width:600px)');
  const [openAlert, setOpenAlert] = useState(false);
  const [eventText, setEventText] = useState('');
  const handleEventClick = (e) => {
    setEventText(e.title);
    setOpenAlert(true);
  };

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpenAlert(false);
  };

  if (props.holidaysList && props.holidaysList.length > 0) {
    if (smallDevice && props.active) {
      const eventList = [];
      const objSmall = JSON.parse(JSON.stringify(props.dateList));
      var indexSmall = 1;
      var totalCountSmall = 0;
      for (let j in objSmall.dateList) {
        totalCountSmall += 1;
      }
      for (let k in objSmall.dateList) {
        var dateSplitSmall = objSmall.dateList[k].split('-');
        var dateStringSmall = dateSplitSmall[2] + '/' + dateSplitSmall[0] + '/' + dateSplitSmall[1];
        var formattedDateSmall = new Date(dateStringSmall);
        eventList.push(
          createEvents(
            `Payment ${indexSmall}/${totalCountSmall}`,
            formattedDateSmall,
            formattedDateSmall
          )
        );
        indexSmall += 1;

        for (let i = 0; i < props.holidaysList.length; i++) {
          var dateSplitSmall2 = props.holidaysList[i][0].split('-');
          var dateStringSmall2 =
            dateSplitSmall2[2] + '/' + dateSplitSmall2[0] + '/' + dateSplitSmall2[1];
          var formattedDateSmall2 = new Date(dateStringSmall2);
          eventList.push(
            createEvents(props.holidaysList[i][1], formattedDateSmall2, formattedDateSmall2)
          );
        }
      }

      return (
        <div style={{ height: '500px', width: '500px', marginTop: '20px', marginBottom: '20px' }}>
          <Calendar
            localizer={localizer}
            defaultDate={dayjs()}
            events={eventList}
            startAccessor='start'
            endAccessor='end'
            style={style}
            onSelectEvent={handleEventClick}
            views={['month', 'agenda']}
          />
          <Snackbar
            anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
            open={openAlert}
            autoHideDuration={4000}
            onClose={handleClose}
          >
            <Alert onClose={handleClose} severity='success' variant='filled' sx={{ width: '100%' }}>
              {eventText}
            </Alert>
          </Snackbar>
        </div>
      );
    } else if (props.active) {
      const eventList = [];
      const obj = JSON.parse(JSON.stringify(props.dateList));
      var index = 1;
      var totalCount = 0;
      for (let i in obj.dateList) {
        totalCount += 1;
      }
      for (let x in obj.dateList) {
        var dateSplit = obj.dateList[x].split('-');
        var dateString = dateSplit[2] + '/' + dateSplit[0] + '/' + dateSplit[1];
        var formattedDate = new Date(dateString);
        eventList.push(
          createEvents(`Payment ${index}/${totalCount}`, formattedDate, formattedDate)
        );
        index += 1;
      }
      for (let i = 0; i < props.holidaysList.length; i++) {
        var dateSplitSmall2 = props.holidaysList[i][0].split('-');
        var dateStringSmall2 =
          dateSplitSmall2[2] + '/' + dateSplitSmall2[0] + '/' + dateSplitSmall2[1];
        var formattedDateSmall2 = new Date(dateStringSmall2);
        eventList.push(
          createEvents(props.holidaysList[i][1], formattedDateSmall2, formattedDateSmall2)
        );
      }

      return (
        <div style={{ height: '850px', width: '1000px', marginTop: '20px', marginBottom: '20px' }}>
          <Calendar
            localizer={localizer}
            defaultDate={dayjs()}
            events={eventList}
            startAccessor='start'
            endAccessor='end'
            style={style}
            onSelectEvent={handleEventClick}
            views={['month', 'agenda']}
          />
          <Snackbar
            anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
            open={openAlert}
            autoHideDuration={4000}
            onClose={handleClose}
          >
            <Alert onClose={handleClose} severity='success' variant='filled' sx={{ width: '100%' }}>
              {eventText}
            </Alert>
          </Snackbar>
        </div>
      );
    } else {
      return null;
    }
  }
}
export default CalendarPage;
