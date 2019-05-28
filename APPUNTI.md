echo "# test_docker" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ZadoFex/test_docker.git
git push -u origin master


 docker build -t ct .

 docker run ct