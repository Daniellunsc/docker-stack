const proxy = require('http-proxy-middleware')
    
module.exports = function(app) {
  app.use(proxy('/todo', {target: 'http://localhost:5002'}))
  app.use(proxy('/auth', {target: 'http://localhost:5001'}))
}