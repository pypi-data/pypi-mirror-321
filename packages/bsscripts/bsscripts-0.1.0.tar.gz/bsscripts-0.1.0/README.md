# BSScripts

BSScripts is a collection of scripts that simplifies and partially automates grading assignments in the Brightspace LMS.
Submissions are downloaded via the Brightspace API and can be distributed to graders in a structured way.
Potentially, some preprocessing can be done on the submissions before they are distributed to graders. 

Graders will receive an archive containing all submissions they were assigned to grade, and can write their feedback in a `feedback.txt` file (with partial Markdown support).
They can do so on their local machine, using any tools they prefer, without the need to interact with the Brightspace LMS web interface.
Once they are done, they can upload their feedback via the Brightspace API.

More specifically, submissions are downloaded, and after potential preprocessing, an encrypted `.7z` archive is created for each grader containing the submissions they are assigned to grade.
There are several strategies to distribute submissions to graders, such as randomly or according to Brightspace group registration.
The archives are then uploaded to a shared file storage location using SCP.
The password to decrypt the archive is sent to the grader via email.
Apart from Brightspace access, the scripts thus require access to an SMTP server (to send the emails) and an SCP shar to store the feedback archives.
All graders should have access to this SCP share in order to download the feedback archives.
The SMTP server, obviously, only needs to be accessible by the distributor.

## Installation
The scripts are written in Python and should run with python 3.10 and higher.

To install, simply run

```bash
pip install bsscripts
```

Apart from that, the following OS packages are required:
- `7za` to create the encrypted archives
- `libreoffice` to convert .docx files to .pdf files (optional)
- `ssh` and `scp` to upload the archives to the shared file storage (often, these are isntalled by default)

## Running
Run the scripts by executing `bsscripts`, after configuring it as explained below.

This will open a dedicated CLI. Type `help` to see the available commands.

Notice that on first startup, you will need to authenticate with Brightspace. 
Perform the instructions on the screen to do so.

## Configuration
`bsscripts` uses configuration files to store settings and credentials. 
These files should be stored in a `./data/config/` directory, and should be named `api.json`, `app.json` and `smtp.json` for the Brightspace API, application and SMTP settings respectively.
More information on the contents of these files can be found below, or in the `/bsscripts/data/scheme/` directory that contains JSON schema files for these configuration files.

### `api.json`
This file configures communication with the Brightspace API.
An example of the `api.json` file can be found below. 

```json
{
  "appId": "...",
  "appKey": "...",
  "lmsUrl": "brightspace.example.com",
  "clientAppUrl": "http://redirect.example.com/trustedUrl",
  "leVersion": "1.79",
  "lpVersion": "1.47"
}
```

The settings should match those of a registered API application in your Brightspace LMS.

### `app.json`
This file configures how the application should behave. 
It contains course-specific settings, such as the course ID, aliases for assignments, grading settings, et cetera.

```json
{
  "tag": "bsscripts", // tag for the identity manager, only required if you need to use multiple identities to authenticate to the Brightspace API
  "courseName": "Sandbox Course 2025", // name of the course in Brightspace
  "course": "sandbox", // internal alias for the course
  "assignmentDefaults": { // default grading settings for assignments
    "ignoredSubmissions": [], // submission ids to ignore
    "draftFeedback": false, // whether to upload feedback as draft or publish it immediately
    "defaultCodeBlockLanguage": "java", // default language for code blocks in feedback
    "fileHierarchy": "smart", // whether to keep the `original` submission's file hierarchy, `flatten`, or unpack in a `smart` way
    "division": { // how to divide the feedback archive
      // ... see below
    },
    "gradeAliases": { // aliases for grades, used in feedback
      "f": "Fail", // entering "f" as grade will be replaced by "Fail" in the feedback
      "i": "Insufficient",
      "s": "Sufficient",
      "g": "Good"
    },
    "removeFiles": [ // files to remove from submissions
      ".*",
      "*.exe",
      "*.jar",
      "*.a",
      "*.o",
      "*.class",
      "*.obj"
    ],
    "removeFolders": [ // folders to remove from submissions
      "__MACOSX",
      "__pycache__",
      ".*"
    ]
  },
  "assignments": { // assignments that should be graded
    "a1": { // 'a1' is the alias for this assignment which can be used in the scripts
      "name": "test assignment" // the name of the assignment in Brightspace
    } // this can also contain the same settings as `assignmentDefaults` to override them for a specific assignment
  },
  "graders": { // who are the graders for this course
    "grader1": { // 'grader1' is the alias for this grader which can be used in the scripts
      "distributeUsername": "grader1", // the username of this grader on the SMB share
      "distributeEmail": "grader1@example.com", // the email address that should receive the feedback archive
      "name": "Grader 1", // the display name of the grader
      "contactEmail": "grader1@example.com" // the email of the grader that will be used in the feedback to 
    }
  }, 
  "distribute": {
    "distributor": "someuser", // the username to login to the SCP share
    "host": "filestorage.example.com", // the hostname of the SCP share
    "share": "/vol/share/someAssignment/assignments" // the path to the share where the feedback archives should be stored
  }
}
```

### `smtp.json`
This file configures the SMTP server that should be used to send emails.
```json
{
  "host": "smtp.example.com",
  "port": 587,
  "username": "someuser",
  "password": "<PASSWORD>",
  "from": "Some User <someuser@example.com>"
}
```


## Division strategies
There are several strategies to divide submissions to graders.
- `random`: submissions are divided randomly to graders
- `brightspace`: submissions are divided according to Brightspace groups (depending on which group the submitter is in, it will be divided to the corresponding grader)
- `persistent`: submissions are divided according to a persistent mapping of students to graders
- `custom`: a custom division strategy can be implemented as a `CourseModule`

### Random division
The random division strategy is the simplest division strategy.
Everytime you distribute submissions, they are randomly assigned to graders as specified in the `graders` field.
You should configure the following settings in the `app.json` file to use this strategy:
```json
{
  "division": {
    "strategy": "random",
    "graderWeights": {
      "grader1": 1,
      "grader2": 2 // grader 2 will receive twice as many submissions as grader 1 in this case
    }
  }
}
```

### Brightspace division
The Brightspace division strategy divides submissions according to Brightspace groups.
You should configure the following settings in the `app.json` file to use this strategy:
```json
{
  "division": {
    "strategy": "brightspace",
    "groupCategoryName": "Grading Groups",
    "groupMapping": {
      "Grading Group 1": "grader1",
      "Grading Group 2": "grader2"
    }
  }
}
```

### Persistent division
Make a random division once and store it in a file, so that the same division can be used in the future.
```json
{
  "division": {
    "strategy": "persistent", 
    "groupCategoryName": "grading-groups", // how to store the division
    "graderWeights": {
      "grader1": 1, 
      "grader2": 2 // grader 2 will receive twice as many submissions as grader 1 in this case
    }
  }
}
```

### Custom division
You can implement your own division strategy by creating a Python script as a `CourseModule`.
Place the script in `./data/course/<course>/plugin.py`.


