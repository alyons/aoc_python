# Advent of Code 2021

Language: Python (3.10)

install Python 3.10
ensure python3 points to python3.10
install python3.20-venv


`source ./bin/activate` -> Enter virtual environment
`pip3 install -e .` - With configuration will set up library in editable mode  
`pip3 install -r ./requirements_dev.txt` - Install Dev Dependancies  
`mypy src` to validate code writing  
`flake8 src` to lint  
`pytest` to run tests  

### To Do:

- [X] Make it so I am doing an import of the package rather than directly calling files
- [X] Complete all 50 stars
- [ ] Clean Up Code
  - [X] Create a generic AdventOfCodeUtils package (parse_file, manhattan_distance, a_star, etc.)
  - [ ] Move specific parse functions to their respective days
  - [ ] Make a* completely generic
- [ ] Add Test Coverage
  - [ ] Get as close to 100% as possible
  - [ ] Move logic to 'main' where appropriate
- [ ] Create default rich layout
  - [X] Add to AdventOfCodeUtils
  - [ ] Work on full screen Layouts
    - [ ] Header
    - [ ] Footer
    - [ ] Data Display
    - [ ] Debug Stats
    - [ ] Random Information
- [ ] Update code to be able to use rich layout
- [ ] Add Advent of Code Badges
- [ ] Add 2019
- [ ] Add 2020
- [ ] Submit answers on build (?)

## Random Notes:

- https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
- https://github.com/marketplace/actions/aoc-badges
