import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import React, { useState, useEffect } from 'react';
import Drawer from '@mui/material/Drawer';
import FormatListNumberedIcon from '@mui/icons-material/FormatListNumbered';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import HelpIcon from '@mui/icons-material/Help';
import { NavLink } from 'react-router-dom';

function NavBar() {
  const [openDrawer, setOpenDrawer] = React.useState(false);

  const drawerList = () => {
    return (
      <Box sx={{ width: 250 }} onClick={toggleDrawer}>
        <List>
          <ListItem key={'List View'} disablePadding sx={{ marginTop: '15px' }}>
            <NavLink
              to='/'
              style={({ isActive }) => {
                return {
                  backgroundColor: isActive ? '#e0e0e0' : '',
                  textDecoration: 'none',
                  color: 'inherit',
                  width: 'inherit',
                };
              }}
              end
            >
              <ListItemButton>
                <ListItemIcon>
                  <FormatListNumberedIcon />
                </ListItemIcon>
                <ListItemText primary={'List View'} />
              </ListItemButton>
            </NavLink>
          </ListItem>
          <ListItem key={'Calendar View'} disablePadding sx={{ marginTop: '15px' }}>
            <NavLink
              to='/calendar'
              style={({ isActive }) => {
                return {
                  backgroundColor: isActive ? '#e0e0e0' : '',
                  textDecoration: 'none',
                  color: 'inherit',
                  width: 'inherit',
                };
              }}
              end
            >
              <ListItemButton>
                <ListItemIcon>
                  <CalendarMonthIcon />
                </ListItemIcon>
                <ListItemText primary={'Calendar View'} />
              </ListItemButton>
            </NavLink>
          </ListItem>
        </List>
        <List sx={{ position: 'absolute', bottom: 0, width: 'inherit' }}>
          <ListItem key={'Help'} disablePadding>
            <NavLink
              to='/help'
              style={({ isActive }) => {
                return {
                  backgroundColor: isActive ? '#e0e0e0' : '',
                  textDecoration: 'none',
                  color: 'inherit',
                  width: 'inherit',
                };
              }}
              end
            >
              <ListItemButton>
                <ListItemIcon>
                  <HelpIcon />
                </ListItemIcon>
                <ListItemText primary={'Help'} />
              </ListItemButton>
            </NavLink>
          </ListItem>
        </List>
      </Box>
    );
  };

  const toggleDrawer = () => {
    setOpenDrawer((oldState) => !oldState);
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position='static'>
        <Toolbar>
          <IconButton
            size='large'
            edge='start'
            color='inherit'
            aria-label='menu'
            onClick={toggleDrawer}
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>
          <Drawer open={openDrawer} onClose={toggleDrawer}>
            {drawerList()}
          </Drawer>
          <Typography variant='h6' component='div' sx={{ flexGrow: 1 }}>
            Payment Scheduler
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
export default NavBar;