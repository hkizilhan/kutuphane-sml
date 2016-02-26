Kullanıcı: <b>{{ get('user_full_name', 'USER_ERROR') }} </b>
&nbsp;&nbsp;&nbsp;<a href="/logout">&Ccedil;ıkış</a>
<hr />

%if is_admin:
<div>
<span>Admin: </span>
<a href="/update_users">Kullanıcıları Güncelle</a>
</div>

<hr />
%end


