##
## EPITECH PROJECT, 2024
## Trade
## File description:
## Makefile of the project
##

NAME = trade

all: $(NAME)

$(NAME):
	cp src/main.py $(NAME)
	chmod 775 $(NAME)

clean:
	rm -rf __pycache__

fclean: clean
	rm -f $(NAME)

re: fclean all

tests_run:
# TODO

IMAGE	= epitechcontent/epitest-docker

docker:
	sudo docker run -it -v $(shell pwd):/app --workdir /app $(IMAGE)
