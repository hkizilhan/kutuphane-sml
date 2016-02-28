% include('tpl/i_logged_user.tpl')

<div class="container">

<div class="row">
  <div class="col-md-6">




<div class="panel panel-info panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">ÖĞRENCİ BİLGİSİ</h3>
  </div>
  <div class="panel-body">
    {{ cur_data[2] }} &nbsp;&nbsp;&nbsp; {{ cur_data[1] }} &nbsp;&nbsp;&nbsp; {{ cur_data[3] }}
  </div>
</div>

% if has_book:
<div class="panel panel-info panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">ÖDÜNÇ ALINAN KİTAP</h3>
  </div>
  <div class="panel-body">
    {{ogr_book[8]}}

  <br><br>
  <form action="/iade" method="post" name="frm_iade" onsubmit="return confirm_delete();">

  <input type="hidden" name="odunc_id" value="{{ ogr_book[0] }}"/>
  <input name="submit" type="submit" value="İade Et" class="btn btn-success"/>

  </form>

    <script>
       function confirm_delete() { return confirm("Kitap iade edilecek, emin misiniz?"); }
    </script>

  </div>
</div>
% end


% if not has_book:

<div class="panel panel-info panel-default">
  
  <div class="panel-body">
    
    <form class="form-horizontal" action="/ogrenci/oduncver" method="post" enctype="multipart/form-data" accept-charset="UTF-8">
  
  <div class="form-group">
    <label for="kitap" class="col-sm-5 control-label">Kitap Adını Girin</label>
    <div class="col-sm-7">
      <input name="kitap" type="text"  class="form-control">
      
      <input type="hidden" name="ogr_no" value="{{ cur_data[1] }}"/>
      <input type="hidden" name="ogr_sinif" value="{{ cur_data[2] }}"/>
      <input type="hidden" name="ogr_adsoyad" value="{{ cur_data[3] }}"/>
    </div>
  </div>
  
      
  <div class="form-group">
    <div class="col-sm-offset-5 col-sm-4">
      <button type="submit" class="btn btn-primary">Kaydet</button>
    </div>
  </div>

</form>
    
    
  </div>
</div>


% end

<br><br>
<a href="/" class="btn btn-primary"> < GERİ DÖN</a>

<div></div>


