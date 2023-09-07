import { Outlet } from 'react-router-dom';
import NavBar from '../components/NavBar';

function HelpWrapper() {
  return (
    <>
      <NavBar />
      <Outlet />
    </>
  );
}
export default HelpWrapper;
