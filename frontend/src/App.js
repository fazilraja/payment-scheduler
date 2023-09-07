import React from 'react';
import NavBar from './components/NavBar';
import Form from './components/Form';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import ListPage from './pages/List';
import CalendarPage from './pages/Calendar';
import Wrapper from './pages/Wrapper';
import HelpPage from './pages/Help';
import HelpWrapper from './pages/HelpWrapper';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Wrapper />,
    children: [
      { path: '/', element: <ListPage /> },
      { path: '/calendar', element: <CalendarPage /> },
    ],
  },
  {
    path: '/help',
    element: <HelpWrapper />,
    children: [{ path: '', element: <HelpPage /> }],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
