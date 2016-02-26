<div>Kullanıcı: {{ get('user', 'USER_ERROR') }}  -  {{ get('user_full_name', 'USER_ERROR') }}</div>
<div></div>
<div><a href="/logout">Kullanıcı &Ccedil;ıkış</a></div>
<hr />




%if is_admin:

<div>
 
<span>Admin: </span>
<a href="/update_users">Kullanıcıları Güncelle</a>
</div>

<hr />

%end


