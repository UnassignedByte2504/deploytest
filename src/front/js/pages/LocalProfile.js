import React from "react";
import { Box } from "@mui/system";
import { CardLocal } from "../component/LocalesCard/CardLocal.jsx";
import { CardLocalProfile } from "../component/card/CardLocalProfile.jsx";
import Grid from "@mui/material/Grid"; // Grid version 1
import Grid2 from "@mui/material/Unstable_Grid2"; // Grid version 2
import { Divider, Typography, useTheme } from "@mui/material";
import { locales } from "../mockingData";

export const LocalProfile = () => {
  const theme = useTheme();
  return (
    <>
      <Box className="container-fluid profile-header">
        <img
          className="image-header"
          src="https://images.unsplash.com/photo-1593167751520-95a058b903c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
        />
      </Box>

      <Box className="container ">
        {/* <Grid container spacing={2}>
          <Grid xs={12} sm={3} className="container-card">
            <CardLocalProfile />
          </Grid>
          <Grid xs={12} sm={6} className="container-contenido" sx={{backgroundColor: theme.palette.background.card, margin:"2rem", padding:"1rem", marginTop:"3rem"}}>
            <Box>
              
            </Box>
          </Grid>
        </Grid> */}
        <div className="row">
          <div className="col-lg-4 container-card">
            <CardLocalProfile
              local_img={locales[1].local_img}
              name={locales[1].name}
              ubicacion_local={locales[1].ubicacion_local}
              city={locales[1].city}
              description={locales[1].description}
              generosMusica={locales[1].generosMusica}
            />
          </div>
          <div className="col-lg-8 container-contenido">
            <Box
              className="contenido-localprofile"
              sx={{ backgroundColor: theme.palette.background.card }}
            >
              <Typography variant="h3">Nuestro estilo</Typography>
              <Divider />

              <Typography className="mt-3" variant="body1">
                Lorem Ipsum es simplemente el texto de relleno de las imprentas
                y archivos de texto. Lorem Ipsum ha sido el texto de relleno
                est??ndar de las industrias desde el a??o 1500, cuando un impresor
                N. del T. persona que se dedica a la imprenta desconocido us??
                una galer??a de textos y los mezcl?? de tal manera que logr?? hacer
                un libro de textos especimen. No s??lo sobrevivi?? 500 a??os, sino
                que tambien ingres?? como texto de relleno en documentos
                electr??nicos, quedando esencialmente igual al original.
              </Typography>

              <Typography className="mt-5" variant="h3">
                Galer??a
              </Typography>
              <Divider />

              {/* <Grid container spacing={2}>
                {locales[0].galeria?.map((element, index) => (
                  <Grid xs={12} sm={4} >
                      <img className="imagen-galeria" src={element} />
                  </Grid>
                ))}
              </Grid> */}

              <div className="row">
                {locales[0].galeria?.map((element, index) => (
                  <div className="col-xs-12 col-md-4">
                    <img className="imagen-galeria" src={element} />
                  </div>
                ))}
              </div>
            </Box>
          </div>
        </div>
      </Box>
    </>
  );
};
