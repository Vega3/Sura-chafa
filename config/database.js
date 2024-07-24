const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('mi_app_salud', 'mi_usuario', 'mi_contraseña', {
  host: 'localhost',
  dialect: 'mysql'
});

module.exports = sequelize;
