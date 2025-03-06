<<<<<<< HEAD
provider "google" {
  project     = "apexgcp"
  credentials = file("credentials.json")
  region      = "us-central1"
  zone        = "us-central1-b"
}

resource "google_storage_bucket" "apex_bucket" {
  name          = "apex-solutions-bucket"
  location      = "US"
  storage_class = "STANDARD"
}

resource "google_bigquery_dataset" "apex_dataset" {
  dataset_id    = "apex_dataset"
  friendly_name = "Apex Dataset"
  description   = "Dataset for Apex Solutions Data"
}

resource "google_compute_instance" "my_instance" {
  name         = "terraform-instance"
  machine_type = "e2-micro"
  zone         = "us-central1-b"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }
=======
provider "google" {
  project     = "apexgcp"
  credentials = file("credentials.json")
  region      = "us-central1"
  zone        = "us-central1-b"
}

resource "google_storage_bucket" "apex_bucket" {
  name          = "apex-solutions-bucket"
  location      = "US"
  storage_class = "STANDARD"
}

resource "google_bigquery_dataset" "apex_dataset" {
  dataset_id    = "apex_dataset"
  friendly_name = "Apex Dataset"
  description   = "Dataset for Apex Solutions Data"
}

resource "google_compute_instance" "my_instance" {
  name         = "terraform-instance"
  machine_type = "e2-micro"
  zone         = "us-central1-b"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }
>>>>>>> 3ad4425 (Initial commit)
}