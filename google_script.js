function doPost(e) {  
  var data = JSON.parse(e.postData.contents);  
  var name = data.name;  
  var points = data.points;  
  var sheet = SpreadsheetApp.getActiveSheet();  
  sheet.appendRow([name, points]);  
  if (points  {  
    // Send WhatsApp message  
    // Code for sending message  
  }  
  return ContentService.createTextOutput('OK');  
} 
