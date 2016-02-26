
<div>{{ msg1 }}</div>
<div>{{ msg2 }}</div>


<form class="form-horizontal" action="/" method="post">
<fieldset>
<!-- Form Name -->
<legend>Giriş</legend>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Kullanıcı Adı</label>  
  <div class="col-md-4">
  <input id="textinput" name="username" placeholder="" class="form-control input-md" type="text">
    
  </div>
</div>

<!-- Password input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="passwordinput">Şifre</label>
  <div class="col-md-4">
    <input id="passwordinput" name="password" placeholder="" class="form-control input-md" type="password">
    
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <br>
    <button id="singlebutton" name="singlebutton" class="btn btn-default">Giriş</button>
  </div>
</div>
</fieldset>
</form>
