help:
	@echo
	@echo "💻 APP"
	@echo
	@echo "run:     create db"
	@echo "reset:   rm db"
	@echo

run:
	python3 sl.py

reset:
	rm *.db
