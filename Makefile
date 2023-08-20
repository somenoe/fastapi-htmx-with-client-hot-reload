run:
	uvicorn main:app --reload

tailwind:
	npx tailwindcss -i ./templates/input.css -o ./static/styles.css --watch
