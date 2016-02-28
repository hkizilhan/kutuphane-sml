<!DOCTYPE html>
<html lang="tr">
<head>
   <meta charset="utf-8">
   <link rel="stylesheet" href="/static/bootstrap.min.css">
</head>

<body>
%if get('err_msg', '') != '':
<div class="alert alert-danger" role="alert">{{err_msg}}</div>
%end
<div class="container">

<div class="row">
  <div class="col-md-6">
  
  <br><br><br>
  
  <legend>Giriş</legend>
  
  <form class="form-horizontal" action="/" method="post">
  
  <div class="form-group">
    <label for="username" class="col-sm-4 control-label">Kullanıcı Adı</label>
    <div class="col-sm-5">
      <input name="username" type="text"  class="form-control" id="username">
    </div>
  </div>
  
  <div class="form-group">
    <label for="password" class="col-sm-4 control-label">Şifre</label>
    <div class="col-sm-5">
      <input name="password" type="password" class="form-control" id="password">
    </div>
  </div>
  
    
  <div class="form-group">
    <div class="col-sm-offset-4 col-sm-4">
      <button type="submit" class="btn btn-primary">Giriş</button>
    </div>
  </div>

</form>
  
  
    </div>
  </div>

</div>


</body>
</html>
