import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../styles/index.css";
import imgSignup from "../../img/Bemyre_signup.jpg";
import Logo from "../../img/Bemyre_logo.png";
import { Button } from "@mui/material";
import TextField from "@mui/material/TextField";
import { Formik, useFormik } from "formik";
import * as Yup from "yup";
import { signupSchema } from "../esquemas";
import FlexBetween from "../component/FlexBetween.jsx";

export const Signup = () => {
  const onSubmit = async (values, ax) => {
    console.log(values);
    await ax.resetForm()
  };

  const {
    values,
    errors,
    touched,
    handleChange,
    handleBlur,
    handleSubmit,
    isSubmiting,
  } = useFormik({
    initialValues: {
      email: "",
      confirmEmail: "",
      password: "",
      confirmPassword: "",
      firstName: "",
      lastName: "",
      userName: "",
      confirmUserName: "",
    },
    validationSchema: signupSchema,
    onSubmit,
  });

  return (
    <div className="backgroundSignup">
      <div className="cardSignup">
        <div className="imgSignup imgSignupDisplayNone">
          <img src={imgSignup} alt="Bemyre concert" />
        </div>

        <div className="textSignup">
          <img src={Logo} />

          <form onSubmit={handleSubmit} autoComplete="off" className="textArea">
            <FlexBetween>
              <TextField
                id="firstName"
                label="First name"
                name="firstName"
                values={values.firstName}
                variant="outlined"
                className="m-1"
                onChange={handleChange}
                onBlur={handleBlur}
                error={errors.userName && touched.userName}
                helperText={
                  errors.userName && touched.userName && errors.userName
                }
              />
              <TextField
                id="lastName"
                label="Last name"
                name="lastName"
                values={values.lastName}
                variant="outlined"
                className="m-1"
                onChange={handleChange}
                onBlur={handleBlur}
                error={errors.lastName && touched.lastName}
                helperText={
                  errors.lastName && touched.lastName && errors.lastName
                }
              />
            </FlexBetween>
            <FlexBetween>
              <TextField
                id="userName"
                label="Username"
                name="userName"
                values={values.userName}
                variant="outlined"
                className="m-1"
                onChange={handleChange}
                onBlur={handleBlur}
                error={errors.userName && touched.userName}
                helperText={
                  errors.userName && touched.userName && errors.userName
                }
              />
              <TextField
                id="confirmUserName"
                label="Confirm Username"
                name="confirmUserName"
                values={values.confirmUserName}
                variant="outlined"
                className="m-1"
                onChange={handleChange}
                onBlur={handleBlur}
                error={errors.confirmUserName && touched.confirmUserName}
                helperText={
                  errors.confirmUserName &&
                  touched.confirmUserName &&
                  errors.confirmUserName
                }
              />
            </FlexBetween>

            <TextField
              id="email"
              label="Email"
              name="email"
              values={values.email}
              variant="outlined"
              className="m-1"
              onChange={handleChange}
              onBlur={handleBlur}
              error={errors.email && touched.email}
              helperText={errors.email && touched.email && errors.email}
            />
            <TextField
              id="confirmEmail"
              label="Confirm Email"
              name="confirmEmail"
              values={values.confirmEmail}
              variant="outlined"
              className="m-1"
              onChange={handleChange}
              onBlur={handleBlur}
              error={errors.confirmEmail && touched.confirmEmail}
              helperText={
                errors.confirmEmail &&
                touched.confirmEmail &&
                errors.confirmEmail
              }
            />
            <TextField
              id="password"
              label="Password"
              name="password"
              type="password"
              values={values.password}
              variant="outlined"
              className="m-1"
              onChange={handleChange}
              onBlur={handleBlur}
              error={errors.password && touched.password}
              helperText={
                errors.password && touched.password && errors.password
              }
            />

            <TextField
              id="confirmPassword"
              label="Confirmar Password"
              name="confirmPassword"
              type="password"
              values={values.confirmPassword}
              variant="outlined"
              className="m-1"
              onChange={handleChange}
              onBlur={handleBlur}
              error={errors.confirmPassword && touched.confirmPassword}
              helperText={
                errors.confirmPassword &&
                touched.confirmPassword &&
                errors.confirmPassword
              }
            />
            <Button variant="contained" type="submit" disabled={isSubmiting}>
              Registro
            </Button>
          </form>
          <hr />
          <div className="rrssSignup colorFb">
            <img src="https://assets.stickpng.com/images/60fea6c83d624000048712b7.png" />
            <p className="">Sign Up with Facebook</p>
          </div>
          <div className="rrssSignup ">
            <img src="https://rotulosmatesanz.com/wp-content/uploads/2017/09/2000px-Google_G_Logo.svg_.png" />
            <p className="text-black">Sign Up with Google</p>
          </div>
        </div>
      </div>
    </div>
  );
};