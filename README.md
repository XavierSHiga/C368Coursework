# C368Coursework
Coursework for C368 Foundations of SRE
- The files within myContributionsToApp/ are files that I directly worked on for the application that we were working with in our team environment.
- The files within myContributionsToInfrastructure/ are files that I directly worked on, and files I debugged/used, for the infrastructure of our team's application.
- The files within PythonActivites/ are just some python activities that we worked on during the training, pretty simple stuff.


myContributionsToApp/ includes a file within githubActionWorkflow/ called testflow.yaml.
testflow.yaml was a file that, when setup with our course's AWS ecr and GitHub secrets:
- Ran on any commits to our team branch
- Checked to see if any changes were made to the source code for the four images that made up our app
    - If changes were made, set a flag to rebuild that image
- Checked to see if any changes were made to the releases/ folder
    - If changes were made, set the release flag (a flag to build all images for a release, or if all images had been removed from the registry)
- Ran conditional builds using the flags previously set
    - If release flag was set to true, built all images
    - If release flag was set to false, but image specific flag was set to true, built that image
        - Else, skipped that image
    - Used docker to build the image
        - Using -f to set source dockerfile
        - Using -t to set the image tag (name)
        - Using environment variables to set the AWS registry and repository to push to
- This file was an attempt to demonstrate that a migration from our Jenkins pipeline to a GitHub Actions pipeline would work
    - Meaning it would be possible (could do everything we wanted from Jenkins) and beneficial (could do it faster and within an environment we already used).

