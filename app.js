const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const passport = require('./config/passport');
const sequelize = require('./config/database');

const app = express();

// Middlewares
app.use(bodyParser.json());
app.use(cors());
app.use(passport.initialize());

// Rutas
const authRoutes = require('./routes/auth');
app.use('/auth', authRoutes);

// Conectar a la base de datos y empezar el servidor
sequelize.sync()
  .then(() => {
    app.listen(3000, () => {
      console.log('Servidor corriendo en http://localhost:3000');
    });
  })
  .catch(err => {
    console.error('Error al conectar a la base de datos:', err);
  });
