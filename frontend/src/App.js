import Login from './components/Login';
import './App.css';
import Home from './components/Home';
import Movies from "./components/Movies";
import Community from './components/Community';
// import {Movies, Home, Login} from "./components";
import { Routes, Route } from 'react-router-dom';
import Signup from './components/Signup';

function App() {
  return (
    <>
    <div className="overlayer"></div>
    <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/signup' element={<Signup />} />
        <Route path='/login' element={<Login />} />
        <Route path='/movies' element={<Movies />} />
        <Route path='/community' element={<Community />} />
      </Routes>
    </>
  );
}



export default App;
