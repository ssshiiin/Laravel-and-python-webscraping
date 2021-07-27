<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>
    </head>
    <body>
        <h1>webscraping</h1>
        <form action="/python" method="POST">
            @csrf
            <input type="text" name="search">
            <input type="submit" value="検索する">
        </form>
        <h1>施設情報</h1>
        @foreach($campInfo[0] as $key => $value)
            <tr>
                <th>{{$key}}</th>
                <tr>{{$value}}</tr>
            </tr>
            <br>
        @endforeach
        <h1>営業情報</h1>
        @foreach($campInfo[1] as $key => $value)
            <tr>
                <th>{{$key}}</th>
                <tr>{{$value}}</tr>
            </tr>
            <br>
        @endforeach
    </body>
</html>