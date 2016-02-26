% include('tpl/i_logged_user.tpl')



<h3>ÖĞRENCİ ADI</h3>
{{ cur_data[2] }} &nbsp;&nbsp;&nbsp; {{ cur_data[1] }} &nbsp;&nbsp;&nbsp; {{ cur_data[3] }}


% if has_book:

<h3>ÖDÜNÇ ALINAN KİTAP </h3>
{{ogr_book[8]}}
&nbsp;<br><br><br>
<form action="/iade" method="post" name="frm_iade" onsubmit="return confirm_delete();">

<input type="hidden" name="odunc_id" value="{{ ogr_book[0] }}"/>
<input name="submit" type="submit" value="İade Et" style="height:30px; width:70px" />

</form>

<script>
function confirm_delete() {
    return confirm("Kitap iade edilecek, emin misiniz?");
}
</script>

% end


% if not has_book:

<form action="/ogrenci/oduncver" method="post" name="frm_odunc_ver" enctype="multipart/form-data" accept-charset="UTF-8">

<p>Kitap Adını Girin &nbsp;&nbsp;&nbsp;
<input maxlength="150" name="kitap" size="30" type="text" /></p>

<input type="hidden" name="ogr_no" value="{{ cur_data[1] }}"/>
<input type="hidden" name="ogr_sinif" value="{{ cur_data[2] }}"/>
<input type="hidden" name="ogr_adsoyad" value="{{ cur_data[3] }}"/>

<p><input name="submit" type="submit" value="Kaydet" style="height:30px; width:70px;"/></p>
</form>

% end

<br><br>
<a href="/"> <<-- GERİ D&Ouml;N / İptal</a>

<div></div>


