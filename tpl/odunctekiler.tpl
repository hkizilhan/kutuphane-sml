% include('tpl/i_logged_user.tpl')

<div class="container">
  <div class="row">
    <div class="col-md-8"> 
      <div class="col-md-6">
          <a href="/" class="btn btn-primary">< GERİ DÖN</a>
      </div>
      <div class="col-md-6 text-right">
          <a href="/odunctekiler/csv" class="btn btn-success">İndir</a>
      </div>
    </div>
    
    <div class="col-md-8">  
        <br>
        <br>
        
        <table class="table table-hover table-condensed">
          <caption>Ödünçteki Kitaplar Listesi.</caption>
          <thead>
            <tr>
              <th></th>
              <th colspan="3">Öğrenci Bilgileri</th>
              <th>Kitap Adı</th>
            </tr>
          </thead>
          <tbody>
            % for row in cur_data:
            <tr>
              <th scope="row">{{counter}}</th>
              <td>{{row[1]}}</td>
              <td>{{row[2]}}</td>
              <td>{{row[3]}}</td>
              <td>{{row[8]}}</td>
            </tr>
            % counter+=1
            % end
          </tbody>
        </table>
        
        <br>
        <br>
    </div>
  
    % if counter > 15:    
    <div class="col-md-8"> 
      <div class="col-md-6">
          <a href="/" class="btn btn-primary">< GERİ DÖN</a>
      </div>
      <div class="col-md-6 text-right">
          <a href="/odunctekiler/csv" class="btn btn-success">İndir</a>
      </div>
    </div>  
    % end    
        
        
    </div>
</div>
        
