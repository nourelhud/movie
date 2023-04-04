/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import "./Login.css";
import "bootstrap/dist/css/bootstrap.min.css";
import icon from "../image/icon.png";
import swal from "sweetalert";
import { useState } from "react";
// import {useNavigate} from "react-router-dom";

export default function Login() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  // const navigate = useNavigate();
  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://127.0.0.1:8000/login/', {
        method: 'POST',
        body: JSON.stringify({ name, password }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const userData = {
                id: data.user_id,
                name,
                email,
                password,
            };
            let users = JSON.parse(localStorage.getItem("data")) || [];
            users.push(userData);
            localStorage.setItem("data", JSON.stringify(users));
            setError("");
            // Login successful, redirect to home page
            window.location.href = "/";
        } else {
            // Login failed, show error message here
            console.log(data)
            setError("Failed to login. Please check your username and password.");
        }
    })
    .catch(error => {
        // Handle any errors here
        setError("An error occurred while trying to login.");
    });
};

  const handleAlertClick = () => {
    swal({
      title: "مــــعــــلــــــش هه",
      timer: 4000,
    });
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
            placeholder="Enter Your Name..."
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
              login
            </button>
            <a href="#" id="alert" onClick={handleAlertClick}>
              عارف انك نسيت كلمه السر؟
            </a>
          </div>
        </form>
      </div>
      </section>
    </>
  );
}
