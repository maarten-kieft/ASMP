<?

    $applicationId = $_GET["application_id"];
    $version = $_GET["version"];
    $ipAddress = $_SERVER['REMOTE_ADDR'];

    $servername = "localhost";
    $username = "kieftm_asmp";
    $password = "H@ppy!C0d1ng";
    $dbname = "kieftm_asmp";
    
    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
    
    if(is_null($applicationId)){
        $applicationId = "";
    }

    if(is_null($version)){
        $version = "";
    }

    $sql = "
    INSERT INTO clients (
        application_id,
        version,
        ip_address,
        last_seen
    ) VALUES (
       '".$applicationId."',
       '".$version."',
       '".$ipAddress."',
        now()
    )
    ON DUPLICATE KEY UPDATE 
      last_seen=VALUES(last_seen),
      ip_address=VALUES(ip_address),
      version=VALUES(version)
    ";

    $conn->query($sql)
    $conn->close();
?>
false