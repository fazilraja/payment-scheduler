import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';

function HelpPage() {
  return (
    <Container sx={{ marginTop: '25px', marginBottom: '50px' }}>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={12}>
          <Typography align='center' variant='h3'>
            Frequently Asked Questions
          </Typography>
        </Grid>
        <Grid item xs={12} sm={12}>
          <Accordion>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography style={{ fontWeight: 'bold' }}>What frequencies are accepted?</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography component={'span'}>
                We support the following predefined frequencies:
                <ul>
                  <li>Weekly = 1 week</li>
                  <li>Monthly = 1 month</li>
                  <li>Bimonthly = 2 months</li>
                  <li>Quarterly = 3 months</li>
                  <li>Semiannual = 6 months</li>
                  <li>Annual = 12 months</li>
                </ul>
                We also support custom frequencies in the form of a number followed by either d, w,
                m, or y (representing day, week, month, year). Here are some examples!
                <ul>
                  <li>25d</li>
                  <li>2W</li>
                  <li>4m</li>
                  <li>1Y</li>
                </ul>
              </Typography>
            </AccordionDetails>
          </Accordion>
          <Accordion>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography style={{ fontWeight: 'bold' }}>
                How does the country affect the payment dates?
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography component={'span'}>
                The country field is used to take holidays into account when calculating the payment
                dates. We currently offer support for the following countries:
                <ul>
                  <li>United States</li>
                  <li>South Africa</li>
                  <li>Australia</li>
                  <li>Germany</li>
                  <li>Brazil</li>
                  <li>India</li>
                </ul>
              </Typography>
            </AccordionDetails>
          </Accordion>
          <Accordion>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography style={{ fontWeight: 'bold' }}>
                What are the Business Day Rules?
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography component={'span'}>
                The business rules are used to determine if we should go to the next or previous day
                in case of holiday/weekend (or ignore them altogether)! The options are defined as
                such:
                <ul>
                  <li>Following: Go to the next business day.</li>
                  <li>Preceding: Go to the previous business day.</li>
                  <li>
                    Modified Following: Go to the next business day, but it does not go to the
                    following month, it stops at the last business day of the month.
                  </li>
                  <li>
                    Modified Preceding: Go to the previous business day, but it does not go to the
                    previous month, it stops at the last first day of the month.
                  </li>
                  <li>No Adjustment: Uses the date, even if it is a holiday or weekend.</li>
                </ul>
              </Typography>
            </AccordionDetails>
          </Accordion>
          <Accordion>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography style={{ fontWeight: 'bold' }}>
                What is the End of the Month Rule?
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography component={'span'}>
                If the date is already the end of month, and the rule is active, when you add
                another month, it will go to the end of that month. For example, 'April 30 + month'
                with the End of Month Rule active will be May 31, but it will be May 30 if the End
                of Month Rule is inactive.
              </Typography>
            </AccordionDetails>
          </Accordion>
        </Grid>
      </Grid>
    </Container>
  );
}
export default HelpPage;
