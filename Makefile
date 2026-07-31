.PHONY: serve build deploy clean new-post new-unlisted

serve:
	mkdocs serve

build:
	mkdocs build

deploy: build
	@echo "Upload site/ to your S3 bucket:"
	@echo "  aws s3 sync site/ s3://YOUR-BUCKET --delete"

clean:
	rm -rf site/ .cache/

new-post:
	@read -p "Title: " title && python scripts/new_post.py --title "$$title"

new-unlisted:
	@read -p "Title: " title && python scripts/new_post.py --title "$$title" --unlisted
