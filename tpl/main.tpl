% include('tpl/i_logged_user.tpl')


% setdefault('text', 'No Text')
<h1>{{get('title', 'No Title')}}</h1>
<p> {{ text }} </p>
% if defined('author'):
  <p>By {{ author }}</p>
% end


<div>ANA SAYFA.... </div>

<form action="/ogrenci" method="post" name="frm_ogrenci">
<p>&Ouml;ğrenci Numarası Gir&nbsp;&nbsp;&nbsp;&nbsp; <input maxlength="5" name="ogr_no" size="5" type="text" /></p>

<p><input name="submit" type="submit" value="Giriş" /></p>
</form>



<div></div>


