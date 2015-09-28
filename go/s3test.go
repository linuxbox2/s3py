package main

import (
    "fmt"
    "github.com/aws/aws-sdk-go/aws" 
    "github.com/aws/aws-sdk-go/service/s3"
)

func main() {

    fmt.Println("started")

    region := "10.1.1.220"
    host := "10.1.1.220"
    force_pathstyle := true
    disable_ssl := true
    loglevel := aws.LogDebug
    
    config := &aws.Config{
        Region: &region,
        Endpoint: &host,
        S3ForcePathStyle: &force_pathstyle,
        DisableSSL: &disable_ssl,
        LogLevel: &loglevel,
    }

    // create an S3 handle
    conn := s3.New(config)

    // do it
    var params *s3.ListBucketsInput
    rsp, err := conn.ListBuckets(params)

    if (err != nil) {
            fmt.Println(err.Error())
    } else {
        fmt.Println(rsp)
    }
}
