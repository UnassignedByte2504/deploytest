//Import React
import React, { useEffect } from "react";
import { Link } from "react-router-dom";

//Import Materials
import { Alert, Box, Snackbar, Stack, Typography } from "@mui/material";

export const AlertLogin = () =>{

    useEffect(()=>{
        localStorage.removeItem("alert_login")
    },[])
        
    const alert_login = localStorage.getItem("alert_login")

    return (
        <Box>
            {alert_login ?
            <Stack>
                <Alert severity="error">{alert_login}</Alert>
            </Stack>
            :
            null
            }
        </Box>
    )
}