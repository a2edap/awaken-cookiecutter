cookies:
	cookiecutter --no-input -f . email=first.last@pnnl.gov use_custom_filehandler=yes use_custom_qc=yes

clean:
	rm -rf ingest_name