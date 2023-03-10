//import React
import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";


//Import materials
import { Box, Typography, IconButton } from "@mui/material";
import InstagramIcon from '@mui/icons-material/Instagram';
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';

//Import styles
import "../../styles/index.css"
import bemyrelogo from "../../img/Bemyre_logo.png"
import { Context } from "../store/appContext";
export const Footer = () =>{

    const {store, actions} = useContext(Context)
    return (
        <Box className="footer">
            <Box className=" left"> 
                <Box className="imgfooter">
                    <img src={bemyrelogo}/>
                </Box>
            </Box>
            <Box className="center">
                <Box className="marginfooter mx-3">
                    <Typography><strong>Navegación</strong></Typography>
                    <Link className="linkfooter" to="/home"><Typography>Home</Typography></Link>
                    {store.current_user? 
                    <Link className="linkfooter" to={`/user/${store.current_user}`}><Typography>Perfil</Typography></Link>
                    :
                    null}
                    <Link className="linkfooter" to="/signup"><Typography>Registro</Typography></Link>
                    <Link className="linkfooter" to="/login"><Typography>Inicio sesión</Typography></Link>
                </Box>
                <Box className="mx-3">
                    <Typography><strong>Acerca de</strong></Typography>
                    <Link className="linkfooter" to="/faq"><Typography>Preguntas Frecuentes</Typography></Link>
                    <Link className="linkfooter" to="/faq"><Typography>¿Qué es Bemyre?</Typography></Link>
                    <Link className="linkfooter" to="/faq"><Typography>¿Cómo creo una banda?</Typography></Link>
                    <Link className="linkfooter" to="/faq"><Typography>¿Puedo unirme a banda?</Typography></Link>
                    <Link className="linkfooter" to="/faq"><Typography>Valores y objetivos</Typography></Link>
                </Box>
                <Box className="mx-3">
                    <Typography><strong>Bandas/Locales</strong></Typography>
                    <Link className="linkfooter" to="/"><Typography>Bandas Populares</Typography></Link>
                    <Link className="linkfooter" to="/"><Typography>Cantantes populares</Typography></Link>
                    <Link className="linkfooter" to="/"><Typography>Locales populares</Typography></Link>
                </Box>
            </Box>
            <Box className="right">
                <Box className="m-1 "><a className="text-white mx-2" href="https://www.instagram.com/"><InstagramIcon className="" sx={{fontSize: "2.5rem"}}/></a></Box>
                <Box className="m-1"><a className="text-white mx-2" href="https://www.facebook.com/"><FacebookIcon sx={{fontSize: "2.5rem"}}/></a></Box>
                <Box className="m-1"><a className="text-white mx-2" href="https://twitter.com/"><TwitterIcon sx={{fontSize: "2.5rem"}}/></a></Box>
            </Box>
        </Box>
    )
}