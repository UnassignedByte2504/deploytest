import { TextField, Typography, Box, Button } from "@mui/material";
import { useFormik, Formik } from "formik";
import React, { useContext } from "react";
import { useParams } from "react-router-dom";
import * as Yup from "yup";
import "../../../../styles/index.css";
import { changePasswordSchema } from "../../../esquemas";
import { Context } from "../../../store/appContext";
const UserPasswordManagement = () => {
  const {actions, store} = useContext(Context)
  const params= useParams()
  const username = params.username
  const onSubmit = async (values, ax) => {
    await actions.changePassword(username, values.oldPassword, values.newPassword)
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
      oldPassword: "",
      newPassword: "",
      confirmNewPassword: "",
    },
    validationSchema: changePasswordSchema,
    onSubmit,
  });

  return (
    <Box className="m-2 changepasswordbox">
      <Typography className="my-3" variant="h3">
        Cambiar Contraseña
      </Typography>
      <form
        onSubmit={handleSubmit}
        autoComplete="off"
        className="changepasswordform"
      >
        <TextField
          className="w-100 my-2"
          variant="outlined"
          label="Old password"
          type="password"
          onChange={handleChange}
          name="oldPassword"
          value={values.oldPassword}
          onBlur={handleBlur}
          error={errors.oldPassword && touched.oldPassword}
          helperText={
            errors.oldPassword && touched.oldPassword && errors.oldPassword
          }
        />
        <TextField
          className="w-100 my-2"
          variant="outlined"
          label="New Password"
          type="password"
          onChange={handleChange}
          name="newPassword"
          value={values.newPassword}
          onBlur={handleBlur}
          error={errors.newPassword && touched.newPassword}
          helperText={
            errors.newPassword && touched.newPassword && errors.newPassword
          }
        />
        <TextField
          className="w-100 my-2"
          variant="outlined"
          label="Confirm New Password"
          type="password"
          onChange={handleChange}
          name="confirmNewPassword"
          value={values.confirmNewPassword}
          onBlur={handleBlur}
          error={errors.confirmNewPassword && touched.confirmNewPassword}
          helperText={
            errors.confirmNewPassword &&
            touched.confirmNewPassword &&
            errors.confirmNewPassword
          }
        />
        <Button
          variant="contained"
          type="submit"
          className="my-2 text-white"
          disabled={isSubmiting}
          color="success"
        >
          <strong>Cambiar Contraseña</strong>
        </Button>
      </form>
    </Box>
  );
};

export default UserPasswordManagement;
