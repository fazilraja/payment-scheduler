import { Outlet } from 'react-router-dom';
import NavBar from '../components/NavBar';
import Form from '../components/Form';

function Wrapper() {
  return (
    <>
      <NavBar />
      <Form />
      <Outlet />
    </>
  );
}
export default Wrapper;
