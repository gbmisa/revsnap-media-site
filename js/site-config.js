/* Single source of truth for site-wide values.
   tools/set_site_url.py reads and rewrites SITE.url — keep the shape intact. */
window.SITE = {
  url: "https://revsnapmedia.com",
  name: "RevSnap Media",
  legalName: "RevSnap Media",
  photographer: "Clark Farmer",
  email: "revsnapmedia@gmail.com",
  phone: "",                                 /* TODO: confirm with Clark */
  instagram: "https://www.instagram.com/revsnapmedia/",
  city: "Provo",
  region: "UT",
  serviceArea: ["Provo", "Orem", "Lehi", "Utah County", "Salt Lake City"],
  ogImage: "/images/cars/007-1600.jpg"
};
