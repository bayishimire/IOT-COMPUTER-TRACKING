  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link rel="stylesheet" href="casc.css">
   
  </head>
  </style><body>
      <form action="register.php" method="POST" enctype="multipart/form-data">
          <!-- <input type="text" name="id" placeholder="id" required><br> -->
          <input type="text" name="first_name" placeholder="first_name" required><br>
          <input type="text" name="second_name" placeholder="second_name" required><br>
          <input type="email" name="email" placeholder="Email" required><br>
          <input type="password" name="password" placeholder="password" required><br>
          <input type="text" name="age" placeholder="age" required><br>
          <input type="text" name="serial" placeholder="serial_number" required><br>
          <input type="file" name="photo" accept="image/*" required><br>
          <input type="submit" name="submit" value="submit">
      </form>
  </body>
 </html>