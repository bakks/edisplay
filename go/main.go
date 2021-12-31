package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
	"time"

	"gopkg.in/gographics/imagick.v2/imagick"
)

func main() {
	tmpDir, err := os.MkdirTemp("", "")
	if err != nil {
		log.Fatal(err)
	}
	//defer os.RemoveAll(tmpDir)

	err = nytimes(tmpDir)
	if err != nil {
		log.Fatal(err)
	}
}

func nytimes(tmpDir string) error {
	year, month, day := time.Now().Date()
	url := fmt.Sprintf("https://static01.nyt.com/images/%d/%d/%d/nytfrontpage/scan.pdf", year, month, day)

	filename := fmt.Sprintf("%s/%s", tmpDir, "nytimes.pdf")

	err := DownloadFile(filename, url)
	if err != nil {
		return err
	}

	return pdfToBmp(filename)
}

func pdfToBmp(pdfPath string) error {
	bmpPath := strings.Replace(pdfPath, "pdf", "bmp", 1)

	ret, err := imagick.ConvertImageCommand([]string{
		"convert", "-density", "200", pdfPath, "-crop", "2360x4310+40+190", "-resize", "x1872", "-rotate", "270", bmpPath,
	})
	if err != nil {
		return err
	}
	log.Printf(ret.Meta)
	fmt.Println(bmpPath)

	return nil
}

func DownloadFile(filepath string, url string) error {

	// Get the data
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// Create the file
	out, err := os.Create(filepath)
	if err != nil {
		return err
	}
	defer out.Close()

	// Write the body to file
	written, err := io.Copy(out, resp.Body)
	log.Printf("wrote %s : %d bytes", filepath, written)
	return err
}
