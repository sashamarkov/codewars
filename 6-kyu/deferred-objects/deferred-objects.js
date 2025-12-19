function Deferred() {
  let resolved = false;
  const successHandlers = [];
  const errorHandlers = [];
  
  this.promise = {
    then: function(s, e) {
      if (s) successHandlers.push(s);
      if (e) errorHandlers.push(e);
      return this;
    },
    success: function(s) {
      successHandlers.push(s);
      return this;
    },
    failure: function(e) {
      errorHandlers.push(e);
      return this;
    }
  };
  
  this.resolve = function(data) {
    if (resolved) throw new Error();
    resolved = true;
    successHandlers.forEach(f => f(data));
  };
  
  this.reject = function(data) {
    if (resolved) throw new Error();
    resolved = true;
    errorHandlers.forEach(f => f(data));
  };
}