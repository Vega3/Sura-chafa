const passport = require('passport');
const { Strategy, ExtractJwt } = require('passport-jwt');
const User = require('../models/User');

const opts = {
  jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
  secretOrKey: 'tu_secreto_jwt'
};

passport.use(new Strategy(opts, (jwt_payload, done) => {
  User.findByPk(jwt_payload.id)
    .then(user => {
      if (user) {
        return done(null, user);
      } else {
        return done(null, false);
      }
    })
    .catch(err => done(err, false));
}));

module.exports = passport;
