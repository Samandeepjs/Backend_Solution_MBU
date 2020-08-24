A command-line tool in Python that retrieves posts from https://jsonplaceholder.typicode.com/posts.

The tool has 3 flags total two flags to specify the range to display as well as a one to send the output to a file.

 

get_posts --start [start_post] --end[ end_post ] --out [output_file]

flags:

   --start optional argument specifies beginning of posts range to output default 0

   --end optional argument specifies end of posts range default size( posts returned )

   --out optional argument specifies name of file to output default stdout

 

useage:

   get_post: start 0 end length posts displays posts to terminal

   get_post --start 5: display posts from 5 to end

   get_post --start 5 --end 20 --out temp.dump: retrive posts 5 to 20 and place output content to file name temp.dump