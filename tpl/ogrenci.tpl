% include('tpl/i_logged_user.tpl')



<div>ÖĞRENCİ ADI</div><br>
{{ cur_data[2] }} &nbsp;&nbsp;&nbsp; {{ cur_data[1] }} &nbsp;&nbsp;&nbsp; {{ cur_data[3] }}

<hr />



% if has_book:

Ödünç Alınan Kitap   <br>
{{ogr_book[8]}}      <a href="/iade/{{ogr_book[0]}}"> İade Et</a>

<form action="/iade" method="post" name="frm_iade" onsubmit="return confirm_delete();">

<input type="hidden" name="odunc_id" value="{{ ogr_book[0] }}"/>
<input name="submit" type="submit" value="İade Et" />

</form>

<script>
function confirm_delete() {
    return confirm("Kitap iade edilecek, emin misiniz?");
}
</script>


% end


% if not has_book:

<form action="/ogrenci/oduncver" method="post" name="frm_ogrenci_kayit">

<p>Kitap Adını Girin 
<input maxlength="50" name="kitap" size="50" type="text" /></p>

<input type="hidden" name="ogr_no" value="{{ cur_data[1] }}"/>
<input type="hidden" name="ogr_sinif" value="{{ cur_data[2] }}"/>
<input type="hidden" name="ogr_adsoyad" value="{{ cur_data[3] }}"/>


<p><input name="submit" type="submit" value="Kaydet" /></p>
</form>

% end






<br><br>
<a href="/"> <<-- GERİ D&Ouml;N / İptal</a>

<div></div>


