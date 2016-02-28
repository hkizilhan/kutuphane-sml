% include('tpl/i_logged_user.tpl')


<div class="container">

<div class="row">
  <div class="col-md-6">
  
  <br><br><br>
  
  
  <form class="form-horizontal" action="/ogrenci" method="post">
  
  <div class="form-group">
    <label for="username" class="col-sm-5 control-label">Öğrenci Numarası</label>
    <div class="col-sm-5">
      <input name="ogr_no" type="text"  class="form-control">
    </div>
  </div>
  
      
  <div class="form-group">
    <div class="col-sm-offset-5 col-sm-4">
      <button type="submit" class="btn btn-primary">Giriş</button>
    </div>
  </div>

</form>
  
  
    </div>
  </div>

</div>






