<?php
/**
 * Quickly and easily backup your MySQL database and have the .tgz copied to
 * your Dropbox account.
 *
 * Copyright (c) 2012 Eric Silva
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @author Eric Silva [eric@ericsilva.org] [http://ericsilva.org/]
 * @version 1.0.0
 */

require('DropboxUploader.php');

// location of your temp directory
$tmpDir = "/tmp/";
// username for MySQL
$user = "sqladmin99";
// password for MySQL
$password = "Qzx595";
// database name to backup
$dbName = "wbs_monrovia";
// hostname or IP where database resides
$dbHost = "mysql.monrovia.org";
// the zip file emailed to you will have this prefixed
$prefix = "monroviadb_";

// username for Dropbox
$dropbox_user = "wbs@monrovia.org";
// password for Dropbox
$dropbox_password = "wbs_595";
// Destination folder in Dropbox (folder will be created if doesn't yet exist)
$dropbox_dest = "db_backups";

// Create the database backup file
$sqlFile = $tmpDir.$prefix.date('Y_m_d').".sql";
$backupFilename = $prefix.date('Y_m_d').".tgz";
$backupFile = $tmpDir.$backupFilename;

$createBackup = "mysqldump -h ".$dbHost." -u ".$user." --password='".$password."' ".$dbName." > ".$sqlFile;
//echo $createBackup;
$createZip = "tar cvzf $backupFile $sqlFile";
//echo $createZip;
exec($createBackup);
exec($createZip);

try {
    // Upload database backup to Dropbox
    $uploader = new DropboxUploader($dropbox_user, $dropbox_password);
    $uploader->upload($backupFile, $dropbox_dest,  $backupFilename);
} catch(Exception $e) {
    die($e->getMessage());
}

// Delete the temporary files
unlink($sqlFile);
unlink($backupFile);

?>