export default (input) => {
  var contentType = [
    "application/java-archive",
    "application/EDI-X12",
    "application/EDIFACT",
    "application/javascript",
    "application/octet-stream",
    "application/ogg",
    "application/pdf",
    "application/xhtml+xml",
    "application/x-shockwave-flash",
    "application/json",
    "application/ld+json",
    "application/xml",
    "application/zip",
    "application/x-www-form-urlencoded",
    "audio/mpeg",
    "audio/x-ms-wma",
    "audio/vnd.rn-realaudio",
    "audio/x-wav",
    "image/gif",
    "image/jpeg",
    "image/png",
    "image/tiff",
    "image/vnd.microsoft.icon",
    "image/x-icon",
    "image/vnd.djvu",
    "image/svg+xml",
    " multipart/mixed",
    "multipart/alternative",
    "multipart/related",
    "multipart/form-data",
    " text/css",
    "text/csv",
    "text/html",
    "text/javascript",
    "text/plain",
    "text/xml",
    " video/mpeg",
    "video/mp4",
    "video/quicktime",
    "video/x-ms-wmv",
    "video/x-msvideo",
    "video/x-flv",
    "video/webm",
    "application/vnd.android.package-archive",
    "application/vnd.oasis.opendocument.text",
    "application/vnd.oasis.opendocument.spreadsheet",
    "application/vnd.oasis.opendocument.presentation",
    "application/vnd.oasis.opendocument.graphics",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.mozilla.xul+xml",
  ];

  for (let responses in input) {
    if (input[responses]["content"]) {
      var header = Object.keys(input[responses]["content"]);

      if (!contentType.includes(header[0])) {
        return [
          {
            message: "Invalid Content-Type provided.",
          },
        ];
      }
    } else {
      return [
        {
          message:
            "Content block in the responses section should not be empty.",
        },
      ];
    }
  }
};
