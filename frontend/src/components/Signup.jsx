/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import "./signup.css";
import "bootstrap/dist/css/bootstrap.min.css";
import icon from "../image/icon.png";
import { useState } from "react";
import {useNavigate} from "react-router-dom";
import axios from "axios";
export default function Signup() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/users/create/', {
              name:name,
              email: email,
              password: password,
            })
              .then(response => {
                console.log(response.data);
                // show a success message to the user
              })
              .catch(error => {
                console.log(error);
                // show an error message to the user
              });
    if (validationFirstName &&validationEmail()) {
      const userData = {
        name,
        email,
        password,
      };
      let users = JSON.parse(localStorage.getItem("data")) || [];
      users.push(userData);
      localStorage.setItem("data", JSON.stringify(users));
      navigate("/login");
      setError("");
    }
  };

  const validationFirstName = () => {
    const regx = /^\w{3,8}$/;
    if (regx.test(name)) {
      return true;
    } else {
      setError("Name Invalid...!");
      return false;
    }
  };
  
  const validationEmail = () => {
    const regx = /^[\w-.]+@([\w-]+.)+[\w-]{2,4}$/;
    if (regx.test(email)) {
      return true;
    } else {
      setError("Email Invalid...!");
      return false;
    }
  };

  return (
    <>
      <section className="section">
      <div className="contain">
        {error && <div className="alert alert-danger">{error}</div>}
        <img src={icon} alt="" />
        <form
          action=""
          className="form-class"
          method="post"
          onSubmit={handleSubmit}
        >
          <input
            type="text"
            name="name"
            id="name"
            placeholder="Enter Your name..."
            className=" form-input"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <input
            type="text"
            name="email"
            id="email"
            placeholder="Enter Your Email..."
            className=" form-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            name="password"
            id="password"
            placeholder="Enter Your Password..."
            className=" form-input form-control"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <div className="login">
            <button type="submit" className="login-btn">
              signup
            </button>
            <a href="/login" id="alert" >
              already have an account?
            </a>
          </div>
        </form>
      </div>
      </section>
      
    </>
  );
}