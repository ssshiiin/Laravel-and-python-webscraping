<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PythonController extends Controller
{
    public function scraping(Request $request){
        $searchWord = $request->get("search");
        exec("/usr/bin/python3 /home/ec2-user/environment/webscraping/resources/python/test.py $searchWord", $output, $result_code);
        $arr=json_decode($output[1],true);
        
        return view("index")->with("campInfo", $arr);
    } 
}
